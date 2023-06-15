import React, { useEffect } from "react";
import axios from "axios";
import { ApiUrls, BaseUrl } from "./Shared/ApiUrls";
import { useHistory } from "react-router-dom/cjs/react-router-dom.min";
import { Roles } from "./Shared/constants";

const Protected = () => {
  const history = useHistory();
  //hiting api
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

      if (response.data.role == "admin") {
        window.location.href = "/allcars";
      } else {
        window.location.href = "/cars";
      }
    } catch (error) {
      console.error(error);
    }
  };

  useEffect(() => {
    postData();
  }, []);
  return (
    <div className=" container">
      <div className="row">
        <div className="col-md-10 offset-1 mt-5">
          <h3 className="text-center py-5">You are Welcome </h3>
        </div>
      </div>
    </div>
  );
};

export default Protected;
