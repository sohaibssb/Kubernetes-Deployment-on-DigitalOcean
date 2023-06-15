import { createContext, useState } from "react";

export const PaymentContext = createContext();

export const PaymentContextProvider = ({children})=>{
    const [paymentDetails,setPaymentDetails]= useState()
    return<PaymentContext.Provider value={{paymentDetails,setPaymentDetails}}>
        {children}
    </PaymentContext.Provider>
}