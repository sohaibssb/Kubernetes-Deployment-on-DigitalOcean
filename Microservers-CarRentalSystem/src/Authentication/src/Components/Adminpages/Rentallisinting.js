import { useEffect, useState } from "react";
import DataTable from "react-data-table-component";
import { ApiMethods, ApiUrls } from "../../Shared/ApiUrls";

const Rentallisinting = () => {
  const [rentalDetails, setRentalDetails] = useState();

  const getRentList = async () => {
    try {
      const response = await fetch(ApiUrls.GET_ALL_RENT_CARS, {
        method: ApiMethods.GET,
        headers: {
          access_token: `${localStorage.getItem("accesstoken")}`,
        },
      });
      const res = await response.json();

      if (response.status >= 200 || response.status <= 299) {
        //callback(res.Message, "success");
        setRentalDetails(res);
      } else if (response.status == 401) {
      } else if (response.status >= 402 || response.status <= 499) {
        //callback(res.Message, "warn");
      } else {
        //callback(res.Message, "warn");
      }
    } catch (err) {
      console.log("errror", err);
      // callback("Something went wrong", "error");
    }
  };

  const Columns = [
    {
      name: "Username",
      selector: (row) => (row.username ? row.username : "NA"),
    },
    {
      name: "Date from",
      selector: (row) => (row.dateFrom ? row.dateFrom : "NA"),
    },
    {
      name: "Date to",
      selector: (row) => (row.dateTo ? row.dateTo : "NA"),
    },
    {
      name: "Car Registration no",
      selector: (row) =>
        row.car.registrationNumber ? row.car.registrationNumber : "NA",
    },
    {
      name: "Brand",
      selector: (row) => (row.car.brand ? row.car.brand : "NA"),
    },
    {
      name: "Model",
      selector: (row) => (row.car.model ? row.car.model : "NA"),
    },
    {
      name: "Total rent",
      selector: (row) => (row.payment.price ? row.payment.price : "NA"),
    },
    {
      name: "Payment Status",
      selector: (row) => (row.payment.status ? row.payment.status : "NA"),
    },
  ];

  useEffect(() => {
    getRentList();
  }, []);
  return (
    <div className="container">
      <div className="row">
        {rentalDetails?.length ? (
          <div className="col-md-12">
            <h3 className="heading mt-4">List of cars on rent</h3>
          </div>
        ) : (
          ""
        )}
        <div className="col-md-12">
          <DataTable
            className=""
            fixedHeader
            data={rentalDetails}
            columns={Columns}
            pagination
            subHeader
          />
        </div>
      </div>
    </div>
  );
};
export default Rentallisinting;
