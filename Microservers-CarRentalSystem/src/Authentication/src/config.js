import { OktaAuth } from "@okta/okta-auth-js";

//constants use for okta login
// const oktaAuth = new OktaAuth({
//   issuer: "https://dev-26551516.okta.com/oauth2/default",
//   clientId: "0oa9vs52rl8RkBBPR5d7",
//   redirectUri: "http://0.0.0.0:3000/login/callback",
//   scopes: ["openid" ,"offline_access", "email", "profile" ,],
//   pkce: true,
// });
const oktaAuth = new OktaAuth({
  issuer: `https://${process.env.REACT_APP_OKTA_BASE_URL}/oauth2/default`,
  clientId: `${process.env.REACT_APP_OKTA_CLIENT_ID}`,
  redirectUri: `${process.env.REACT_APP_OKTA_REDIRECTURI}` + "/login/callback",
  scopes: ["openid" ,"offline_access", "email", "profile" ,],
  pkce: false,
});
export default oktaAuth;
