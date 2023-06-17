import { OktaAuth } from "@okta/okta-auth-js";

//constants use for okta login
const oktaAuth = new OktaAuth({
  issuer: "https://dev-26551516.okta.com/oauth2/default",
  clientId: "0oa9vs52rl8RkBBPR5d7",
  redirectUri: "http://0.0.0.0:3000/login/callback",
  scopes: ["openid" ,"offline_access", "email", "profile" ,],
  pkce: true,
});

export default oktaAuth;
