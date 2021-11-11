import { Link } from "react-router-dom";
import Layout from "../Layout";
import axios from "axios";

const Home = () => {
  const handleLogout = async () => {
    await axios.get("user/logout/");
    return (window.location.href = "/login");
  };

  return (
    <Layout>
      <h1>Home Page</h1>
      <Link to="/login">Login</Link>
      <br />
      <br />
      <Link to="/profile">profile</Link>
      <br />
      <br />
      <Link to="/settings">settings</Link>
      <br />
      <br />
      <button onClick={handleLogout}>Logout</button>
    </Layout>
  );
};

export default Home;
