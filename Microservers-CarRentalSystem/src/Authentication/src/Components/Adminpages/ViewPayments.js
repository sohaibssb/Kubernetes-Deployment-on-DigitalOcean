import React, { useEffect, useState } from "react";
import { ApiMethods, ApiUrls } from "../../Shared/ApiUrls";
import DataTable from "react-data-table-component";

const ViewPayments = () => {
  const [users, setUsers] = useState();

  const Columns = [
    {
      name: "Username",
      selector: (row) => (row.username ? row.username : "-"),
      sortable: true,
    },
    {
      name: "Car Id",
      selector: (row) => (row.carID ? row.carID : "-"),
    },
    {
      name: "Payment Id",
      selector: (row) => (row.paymentID ? row.paymentID : "NA"),
    },
    {
      name: "Payment Status",
      selector: (row) => (row.paymentStatus ? row.paymentStatus : ""),
      sortable: true,
    },
    {
      name: "Price",
      selector: (row) => (row.price ? row.price : "-"),
      sortable: true,
    },
  ];

  const getAllUser = async () => {
    try {
      const response = await fetch(ApiUrls.GET_ALL_USER, {
        method: ApiMethods.GET,
        headers: {
          access_token: `${localStorage.getItem("accesstoken")}`,
        },
      });
      const res = await response.json();
      setUsers(res.data);
    } catch (error) {
      console.log(error);
    }
  };

  useEffect(() => {
    getAllUser();
  }, []);
  return (
    <div className="container">
      <div className="row">
        {users?.length ? (
          <div className="col-md-12">
            <h3 className="heading mt-4">List of cars</h3>
          </div>
        ) : (
          ""
        )}
        <div className="col-md-12">
          <DataTable
            className=""
            fixedHeader
            data={users}
            columns={Columns}
            pagination
            subHeader
          />
        </div>
      </div>
    </div>
  );
};

export default ViewPayments;

