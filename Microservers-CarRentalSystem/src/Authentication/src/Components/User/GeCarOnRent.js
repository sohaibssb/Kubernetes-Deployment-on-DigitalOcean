import React, { useContext, useEffect, useState } from "react";
import {
  useHistory,
  useParams,
} from "react-router-dom/cjs/react-router-dom.min";
import { ToastNotification } from "../../Shared/constants";
import { ApiMethods, ApiUrls } from "../../Shared/ApiUrls";
import { useForm } from "react-hook-form";
import { ToastContainer } from "react-toastify";
import { Modal } from "bootstrap";
import { PaymentContext } from "../../Shared/paymentDetails";
import BasicModal from "./Modall";

const GeCarOnRent = () => {
  const { id } = useParams();
  const history = useHistory();
  const { paymentDetails, setPaymentDetails } = useContext(PaymentContext);
  const [car, setCar] = useState();

  const [startDate, setStartDate] = useState("");
  const [endDate, setEndDate] = useState("");
  const [totalPrice, setTotalPrcie] = useState();

  const [open, setOpen] = useState(false);
  const handleOpen = () => setOpen(true);
  const handleClose = () => setOpen(false);

  const {
    reset,
  } = useForm();

  async function getSingleCar(callback) {
    try {
      const response = await fetch(`${ApiUrls.GET_SINGLE_CAR_DETAILS}${id}`, {
        method: ApiMethods.GET,
        headers: {
          access_token: `${localStorage.getItem("accesstoken")}`,
        },
      });
      const res = await response.json();

      if (response.status >= 200 || response.status <= 299) {
        callback(res.Message, "success");
        setCar(res);
      } else if (response.status == 401) {
      } else if (response.status >= 402 || response.status <= 499) {
        callback(res.Message, "warn");
      } else {
        callback(res.Message, "warn");
      }
    } catch (err) {
      console.log("errror", err);
      callback("Something went wrong", "error");
    } 
  }

  const getCars = () => {
    getSingleCar((message, type) => {
      ToastNotification(message, type);
    });
  };

  async function postRentCarDetailsFn(payload, callback) {
    try {
      const response = await fetch(ApiUrls.POST_CAR_ON_RENT, {
        method: ApiMethods.POST,
        body: JSON.stringify(payload),
        headers: {
          access_token: `${localStorage.getItem("accesstoken")}`,
        },
      });

      const res = await response.json();
      
      if (response.status >= 200 || response.status <= 299) {
        setPaymentDetails(res);
        history.push("/payments");
        callback(res.error, "success");
      } else if (response.status == 403 || response.status <= 499) {
        callback("Car is already ordered", "warn");
      } else {
        callback(res.Message, "warn");
      }
    } catch (err) {
      //console.log("errror", err);
      callback("Something went wrong", "error");
    } 
  }

  const calculateDiffrenceInDay = () => {
    const start = new Date(startDate);
    const end = new Date(endDate);
    const diffrence = end.getTime() - start.getTime();
    const differenceInDays = diffrence / (1000 * 3600 * 24);
    setTotalPrcie(differenceInDays * car?.price);
  };

  const submitHandler = (data) => {
    const payload = {
      carUid: id,
      dateFrom: data.dateFrom,
      dateTo: data.dateTo,
    };

    postRentCarDetailsFn(payload, (message, type) => {
      ToastNotification(message, type);
      reset();
    });
  };

  useEffect(() => {
    getCars();
  }, [id]);

  useEffect(() => {
    if (endDate != "" && startDate != "") calculateDiffrenceInDay();
  }, [endDate, startDate]);

  return (
    <><div className="container">
      <div className="row mt-3">
        <div className="col-md-6 offset-3">
        <div class="card border-primary border-3">
        <div class="card-header">Featured</div>
        <div class="card-body">
          <h5 class="card-title">Car Brand : {car?.brand}</h5>
          <p class="card-text">{`Mode of the car is${car?.model}.  `}</p>
          <p class="card-text">{`Car is of type ${car?.type}.`}</p>
          <p class="card-text">
            {`Registraton number is${car?.registrationNumber}`}
          </p>
          <p class="card-text">{`Rent of the car  is ${car?.price}.`}</p>
          <p class="card-text">{`Power of the car  is ${car?.power}`}</p>

          <button className="btn btn-primary" onClick={handleOpen}>Get this Car on Rent</button>
        </div>
      </div>
        </div>
      </div>
    </div>
     

      <ToastContainer />
      <BasicModal
        open={open}
        totalPrice={totalPrice}
        handleClose={handleClose}
        submitHandler={submitHandler}
        setStartDate={setStartDate}
        setEndDate={setEndDate}
        id={id}
      />
    </>
  );
};

export default GeCarOnRent;
