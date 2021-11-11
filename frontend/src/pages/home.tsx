import { Link } from "react-router-dom";
import Layout from "../Layout";

const Home = () => {
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
    </Layout>
  );
};

export default Home;
