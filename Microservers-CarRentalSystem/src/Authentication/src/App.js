import React from "react";
import { SecureRoute, Security, LoginCallback } from "@okta/okta-react";
import { toRelativeUrl } from "@okta/okta-auth-js";
import { Route, useHistory } from "react-router-dom";
import Home from "./Home";
import Protected from "./Protected";
import oktaAuth from "./config";
import Nav from "./Header/Nav";
import CreateCar from "./Components/Adminpages/CreateCarAdmin";
import DisplayCarAdmin from "./Components/Adminpages/DisplayCarAdmin";
import ViewCar from "./Components/User/ViewCar";
import { AuthContextProvider } from "./Shared/auth";
import GeCarOnRent from "./Components/User/GeCarOnRent";
import { PaymentContextProvider } from "./Shared/paymentDetails";
import PaymentSlip from "./Components/User/PaymentSlip";
import ViewPayments from "./Components/Adminpages/ViewPayments";
import Rentallisinting from "./Components/Adminpages/Rentallisinting";

const App = () => {
  const history = useHistory();
  const restoreOriginalUri = async (_oktaAuth, originalUri) => {
    history.replace(toRelativeUrl(originalUri || "/", window.location.origin));
  };

  return (
    <Security oktaAuth={oktaAuth} restoreOriginalUri={restoreOriginalUri}>
      <AuthContextProvider>
        <PaymentContextProvider>
          <Nav />
          <Route path="/" exact={true} component={Home} />
          <SecureRoute path="/protected" component={Protected} />
          <SecureRoute path="/createcar" component={CreateCar} />
          <SecureRoute path="/allcars" component={DisplayCarAdmin} />
          <SecureRoute path="/cars" component={ViewCar} />
          <SecureRoute path="/users" component={ViewPayments} />
          <SecureRoute path="/car/detail/:id" component={GeCarOnRent} />
          <SecureRoute path="/payments" component={PaymentSlip} />
          <SecureRoute path="/rentallisting" component={Rentallisinting} />
          <Route path="/login/callback" component={LoginCallback} />
        </PaymentContextProvider>
      </AuthContextProvider>
    </Security>
  );
};

export default App;
