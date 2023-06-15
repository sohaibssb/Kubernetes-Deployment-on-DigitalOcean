import { useOktaAuth } from "@okta/okta-react/";
import React, { useContext, useEffect, useState } from "react";
import { Link, useHistory } from "react-router-dom/cjs/react-router-dom.min";
import { Roles , Logoutfn } from "../Shared/constants";
import { AdminRoutes, UserRoutes } from "../Components/Routes/Routes";
import { AuthContext } from "../Shared/auth";

const Nav = () => {
  const [role,setRole] = useContext(AuthContext);
  const { oktaAuth, authState } = useOktaAuth();
 
  const history = useHistory();

  useEffect(() => {
    if(localStorage.getItem('role')!=undefined || localStorage.getItem('role')!=null)
    setRole(localStorage.getItem("role"));
  }, []);

  if (!authState?.isAuthenticated) {
    return;
  }

  const logout = () => {
    /* localStorage.removeItem("role");
    localStorage.removeItem("accesstoken");
    oktaAuth.signOut("/");
    history.push("/"); */
    Logoutfn(oktaAuth)
  };

  
  return (
    <nav className="navbar navbar-expand-lg  bg-primary">
      <div className="container-fluid">
        <a className="navbar-brand" href="#">
          OKTA
        </a>
        <button
          className="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNavDropdown"
          aria-controls="navbarNavDropdown"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarNavDropdown">
          <ul className="navbar-nav ms-auto">
            {authState?.isAuthenticated && role!="" && role!=undefined && role!=null ? (
              <>
                {role == Roles?.Admin.toLowerCase() ? (
                  <>
                    {AdminRoutes?.map((item) => {
                      return (
                        <li key={item.title} className="nav-item">
                          <Link className="nav-link" to={item.path}>
                            {item.title}
                          </Link>
                        </li>
                      );
                    })}
                  </>
                ) : (
                  <>
                    {UserRoutes?.map((item) => {
                      return (
                        <li key={item.title} className="nav-item">
                          <Link className="nav-link" to={item.path}>
                            {item.title}
                          </Link>
                        </li>
                      );
                    })}
                  </>
                )}
                <li className="nav-item">
                  <button onClick={logout} className=" nav-link active">
                    Logout
                  </button>
                </li>
              </>
            ) : (
              <></>
            )}
          </ul>
        </div>
      </div>
    </nav>
  );
};

export default Nav;
