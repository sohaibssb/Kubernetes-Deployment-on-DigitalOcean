import React, { useState, useEffect } from "react";
import DataTable from "react-data-table-component";
import { ApiMethods, ApiUrls } from "../../Shared/ApiUrls";
import { Roles, ToastNotification, carData } from "../../Shared/constants";
import { useHistory } from "react-router-dom";
import InfoModal from "../../Shared/InfoModal";
import { ToastContainer } from "react-toastify";

const DrawAction = (available, uid, setOpenModal, setSelectedRowId) => {
  return (
    <button
    disabled={!available}
      onClick={() => {
        setOpenModal(true);
        setSelectedRowId(uid);
      }}
      className="btn btn-danger"
    >
      Delete
    </button>
  );
};

const DisplayCarAdmin = () => {
  const [filterData, setFilterData] = useState();
  const history = useHistory();
  const [openModal, setOpenModal] = useState(false);
  const [selectedRowId, setSelectedRowId] = useState();

  const hitApi = async () => {
    const payload = {
      carUid: selectedRowId,
    };
    console.log(payload, "delete payload");
    try {
      const response = await fetch(ApiUrls.DELETE_CAR, {
        method: ApiMethods.DELETE,
        body: JSON.stringify(payload),
        headers: {
          access_token: `${localStorage.getItem("accesstoken")}`,
        },
      });
      const res = await response.json();
      console.log(response,"erorr")
      if (response.status == 201 || response.status == 200) {
        //callback("Car is deleted Succesfully", "success");
        getAllCars();
        handleClose()
       
       

      } else if (response.status >= 400 || response.status <= 499) {
        ToastNotification(res.Message,"success")
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
      name: "Car Uid",
      selector: (row) => (row.carUid ? row.carUid : "-"),
      sortable: true,
    },
    {
      name: "Brand.",
      selector: (row) => (row.brand ? row.brand : "-"),
    },
    {
      name: "model",
      selector: (row) => (row.model ? row.model : "NA"),
    },
    {
      name: "Registration Number",
      selector: (row) => (row.registrationNumber ? row.registrationNumber : ""),
      sortable: true,
    },
    {
      name: "Power",
      selector: (row) => (row.power ? row.power : "-"),
      sortable: true,
    },
    {
      name: "Type",
      selector: (row) => (row.type ? row.type : "-"),
    },
    {
      name: "Price",
      selector: (row) => (row.price ? row.price : "-"),
    },
    {
      name: "Available",
      selector: (row) => (row.available ? "Availabel" : "Not availabel"),
    },
    {
      name: "Action",
      cell: (row) => {
        return DrawAction(row.available ,row.carUid, setOpenModal, setSelectedRowId);
      },
    },
  ];

  async function getAllCars() {
    try {
      const response = await fetch(ApiUrls.GET_CAR, {
        method: ApiMethods.GET,
        headers: {
          access_token: `${localStorage.getItem("accesstoken")}`,
        },
      });
      const res = await response.json();
        
      if (response.status >= 200 || response.status <= 299) {
        //callback(res.Message, "success");
        ToastNotification(res.Message,"success")
        setFilterData(res.items);
      } else if (response.status == 403) {
        //callback(res.Message, "warn");
        console.log("working")
        ToastNotification("Car cannot be deleted. It is on Rent!", "warn")
      } else {
        //callback(res.Message, "warn");
      }
    } catch (err) {
      console.log("errror", err);
     
    }
  }

  const handleClose = () => {
    setOpenModal(false);
    setSelectedRowId("");
  };

  useEffect(() => {
    getAllCars();
  }, []);
  return (
    <>
      <div className="container">
        <div className="row">
          {filterData?.length ? (
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
              data={filterData}
              columns={Columns}
              pagination
              subHeader
            />
          </div>
        </div>
      </div>
            
      <InfoModal open={openModal} confirm={hitApi} handleClose={handleClose} />
      <ToastContainer/>
    </>
  );
};

export default DisplayCarAdmin;
