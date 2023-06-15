import { toast, ToastContainer } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

export const Roles = {
  User: "user",
  Admin: "admin",
};

export const ToastNotification = (message, type) => {
  toast[type](message, {
    position: toast.POSITION.TOP_CENTER,
  });
};

export const Logoutfn = (oktaAuthfn) => {
  localStorage.clear();
  oktaAuthfn.signOut("/");
  //window.location.href='/'
};

export const carData = [
  {
    carUid: "109b42f3-198d-4c89-9276-a7520a7120ab",
    brand: "Mercedes Benz",
    model: "GLA 250",
    registrationNumber: "ЛО777Х799",
    power: 249,
    type: "SEDAN",
    price: 3500,
    available: true,
  },
  {
    carUid: "109b42f3-198d-4c89-9276-a7520a7120ab",
    brand: "Mercedes Benz",
    model: "GLA 250",
    registrationNumber: "ЛО777Х799",
    power: 249,
    type: "SEDAN",
    price: 3500,
    available: true,
  },
];

export const options = [
    { value: "Select type", label: "Select type" },
  { value: "SEDAN", label: "SEDAN" },
  { value: "SUV", label: "SUV" },
  { value: "MINIVAN", label: "MINIVAN" },
  { value: "ROADSTER", label: "ROADSTER" },
];
