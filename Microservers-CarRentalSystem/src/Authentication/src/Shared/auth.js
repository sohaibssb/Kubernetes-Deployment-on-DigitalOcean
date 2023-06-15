import { createContext, useState } from "react";

export const AuthContext = createContext();

export const AuthContextProvider = ({children})=>{
    const [role,setRole]= useState("")
    return<AuthContext.Provider value={[role,setRole]}>
        {children}
    </AuthContext.Provider>
}