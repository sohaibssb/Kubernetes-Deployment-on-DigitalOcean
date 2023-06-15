import React, { useContext } from "react";
import { PaymentContext } from "../../Shared/paymentDetails";

const PaymentSlip = () => {
  const { paymentDetails, setPaymentDetails } = useContext(PaymentContext);
  
 
  return (
    <div class="container text-center">
      <div className="row mt-5">
        <div className="col-md-6 offset-3">
          <table class="table table-bordered border-primary border-3 border">
            <thead>
              <tr>
                <th colSpan={2} scope="col" className="text-danger h4">
                  Payment details
                </th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <th scope="row">Rental uid</th>
                <td>{paymentDetails?.rentalUid}</td>
              </tr>
              <tr>
                <th scope="row">Username</th>
                <td>{paymentDetails?.username}</td>
              </tr>
              <tr>
                <th scope="row">Car uid</th>
                <td>{paymentDetails?.carUid}</td>
              </tr>
              <tr>
                <th scope="row">Rent started date</th>
                <td>{paymentDetails?.dateFrom}</td>
              </tr>
              <tr>
                <th scope="row">Rent end date</th>
                <td>{paymentDetails?.dateTo}</td>
              </tr>
              <tr>
                <th scope="row">Payment uid</th>
                <td>{paymentDetails?.payment?.paymentUid}</td>
              </tr>
              <tr>
                <th scope="row">Payment </th>
                <td>{paymentDetails?.payment?.price} /-</td>
              </tr>

              <tr>
                <th scope="row">Payment status</th>
                <td>{paymentDetails?.payment?.status}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};

export default PaymentSlip;
