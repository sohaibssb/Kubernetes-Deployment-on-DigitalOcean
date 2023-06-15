import React, { useState } from "react";
import { ToastContainer } from "react-toastify";
import { BaseUrl } from "../../Shared/ApiUrls";
import { Link } from "react-router-dom/cjs/react-router-dom.min";

const IndivualCars = ({ posts }) => {
  return (
    <>
      {posts?.map((item) => {
        return (
          <>
            <React.Fragment key={item.id}>
              <div className="col-md-3 mx-4">
                <div className="card border-3 border-primary">
                  <div className="card-body">
                    <h5 className="card-title">Car Model : {item?.model}</h5>
                    <h6 className="card-subtitle mb-2 text-body-secondary">
                      {item.type}
                    </h6>
                    <hr/>
                    <p className="card-text">
                      {`The car have model name ${item?.model} ,it is of type ${item?.type} and its uid number is ${item?.carUid} If you want to get it on rent please click on the follwin button`}
                      .
                    </p>
                    <Link
                      className="btn btn-primary"
                      to={`/car/detail/${item?.carUid}`}
                    >
                      View Details
                    </Link>
                  </div>
                </div>
              </div>
            </React.Fragment>
          </>
        );
      })}
      <ToastContainer />
    </>
  );
};

export default IndivualCars;
