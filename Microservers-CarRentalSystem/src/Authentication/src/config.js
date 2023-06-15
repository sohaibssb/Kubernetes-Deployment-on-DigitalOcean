import { OktaAuth } from "@okta/okta-auth-js";

//constants use for okta login
const oktaAuth = new OktaAuth({
  issuer: `https://${process.env.REACT_APP_OKTA_BASE_URL}/oauth2/default`,
  clientId: `${process.env.REACT_APP_OKTA_CLIENT_ID}`,
  redirectUri: `${process.env.REACT_APP_OKTA_REDIRECTURI}` + "/login/callback",
  scopes: ["openid" ,"offline_access", "email", "profile" ,],
  pkce: true,
});

export default oktaAuth;
