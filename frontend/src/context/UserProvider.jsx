import { useState } from "react";
import { UserContext } from "./context";

const user = JSON.parse(localStorage.getItem('user'))

export const UserProvider = ({ children }) => {
    const [isLogin, setLogin] = useState(user != null)
    const toggleLogin = () => {
        setLogin(!isLogin)
    }

    return (
        <UserContext.Provider value={{ isLogin, toggleLogin }}>
            {children}
        </UserContext.Provider>
    )
}