import React, { useContext } from "react";
import { useOktaAuth } from "@okta/okta-react";
import { useHistory } from "react-router-dom";
import axios from "axios";
import { ApiUrls } from "./Shared/ApiUrls";
import { AuthContext } from "./Shared/auth";
import Loader from "./assests/Gear.gif";
import "./assests/style.css"

const Home = () => {
  const { oktaAuth, authState } = useOktaAuth();
  const history = useHistory();
  const login = async () => oktaAuth.signInWithRedirect();
  const [role, setRole] = useContext(AuthContext);

  if (!authState) {
    return <div>Loading...</div>;
  }

  const postData = async () => {
    
    try {
      const obj = JSON.parse(localStorage.getItem("okta-token-storage"));
      const payload = {
        accessToken: obj.accessToken.accessToken,
        refreshToken: obj.refreshToken.refreshToken,
      };
      const response = await axios.post(ApiUrls.LOGIN_CAR, payload);
      localStorage.setItem("role", response.data.role);
      localStorage.setItem("accesstoken", response.data["access token"]);
      setRole(response.data.role);
      if (response.data.role == "admin") {
        //window.location.href = "/allcars";
        history.push("/allcars");
      } else {
        //window.location.href = "/cars";
        history.push("/cars");
      }
    } catch (error) {
      console.error(error);
    }
  };

  if (authState.isAuthenticated) {
    postData();
  }
  if (authState.isAuthenticated) {
    return (
      <div className="loader-i">
        <img style={{height:'80px',width:'80px'}} className="text-center" src={Loader} />
      </div>
    );
  }

  return (
    <div className=" container">
      <div className="row">
        <div className=" col-md-6 m-auto mt-5">
          <div className="card bg-light-subtle">
            <div className="card-body">
              <h5 className="card-title">Not Logged in yet</h5>
              <button className="btn btn-primary" onClick={login}>
                Login
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Home;
