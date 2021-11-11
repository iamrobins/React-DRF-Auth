import { useEffect, useState } from "react";
import { Link, Navigate } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { saveUser } from "../state";
import axios from "axios";

const Login = () => {
  const [email, setEmail] = useState<string>();
  const [password, setPassword] = useState<string>();
  const dispatch = useDispatch();
  const { user } = useSelector((state: any) => state.user);
  const [redirect, setRedirect] = useState<boolean>(false);

  useEffect(() => {
    if (user?.email) return setRedirect(true);
  }, [user]);

  const handleLogin = async (e: any) => {
    e.preventDefault();
    try {
      const { data } = await axios.post("user/login/", {
        email: email,
        password: password,
      });
      dispatch(saveUser(data));
      setRedirect(true);
    } catch {
      setRedirect(false);
    }
  };

  if (redirect) return <Navigate to="/" />;

  return (
    <div>
      <h1>Login Page</h1>
      <br />
      <br />
      <br />
      <form onSubmit={handleLogin}>
        <input
          type="email"
          placeholder="email@email.com"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
        <input
          type="password"
          placeholder="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <button type="submit">Login</button>
      </form>
      <Link to="/">Home</Link>
    </div>
  );
};

export default Login;
