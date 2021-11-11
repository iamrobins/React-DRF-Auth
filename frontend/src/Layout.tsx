import { useEffect, useState } from "react";
import axios from "axios";
import { Navigate } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { saveUser } from "./state";

const Layout = (props: any) => {
  const [redirect, setRedirect] = useState(false);
  const dispatch = useDispatch();
  const { user } = useSelector((state: any) => state.user);

  useEffect(() => {
    if (user?.email) return;

    (async () => {
      try {
        const { data } = await axios.get("user/user/");
        dispatch(saveUser(data));
      } catch (e) {
        setRedirect(true);
      }
    })();
  }, [user?.email, dispatch]);

  if (redirect) {
    return <Navigate to={"/login"} />;
  }

  return props.children;
};

export default Layout;
