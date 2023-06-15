import { useEffect, useState } from "react";
import { ToastContainer } from "react-toastify";
import { ApiMethods, ApiUrls } from "../../Shared/ApiUrls";
import { Logoutfn, ToastNotification } from "../../Shared/constants";
import IndivualCars from "./IndivualCar";
import { carData } from "../../Shared/constants";
import { useOktaAuth } from "@okta/okta-react";

const ViewCar = () => {
  const [carList, setCarList] = useState();
  const [loader, setLoader] = useState(false);
  const { oktaAuth } = useOktaAuth();

  async function getAllCars(callback) {
    try {
      setLoader(true);
      const response = await fetch(ApiUrls.GET_CAR_USER, {
        method: ApiMethods.GET,
        headers: {
          access_token: `${localStorage.getItem("accesstoken")}`,
        },
      });
      const res = await response.json();

      if (res.message == "Invalid Token") {
        Logoutfn(oktaAuth);
      }
      if (response.status >= 200 || response.status <= 299) {
        callback(res.Message, "success");
        setCarList(res.items);
      } else if (response.status >= 400 || response.status <= 499) {
        callback(res.Message, "warn");
      } else {
        callback(res.Message, "warn");
      }
    } catch (err) {
      callback("Something went wrong", "error");
    } finally {
      setLoader(false);
    }
  }

  const getCars = () => {
    getAllCars((message, type) => {
      ToastNotification(message, type);
      if (type == "error") {
        /*  dispatch(AuthRemove()); */
      }
    });
  };

  useEffect(() => {
    getCars();
  }, []);

  return (
    <>
      <div className="row mt-5">
        <IndivualCars posts={carList} />
      </div>
      <ToastContainer />
    </>
  );
};

export default ViewCar;
