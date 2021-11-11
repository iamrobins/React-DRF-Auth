// import axios from "axios";

// export default axios.create({
//   baseURL: "http://localhost:8000/api/",
//   withCredentials: true,
// });

// let accessToken = localStorage.getItem("access");

// axios.defaults.baseURL = "http://localhost:8000/api/";
// axios.defaults.withCredentials = true;
// axios.defaults.headers.common["Authorization"] = "Bearer " + accessToken;

// axios.interceptors.request.use(async (req: any) => {
//   if (!accessToken) {
//     accessToken = localStorage.getItem("access");
//     axios.defaults.headers.common["Authorization"] = "Bearer " + accessToken;
//   }

//   const token = decodeJWT(localStorage.getItem("access") || "");

//   if (!token) return req;

//   const isExpired = new Date(token.exp * 1000) < new Date();
//   console.log(isExpired);
//   if (!isExpired) return req;

//   // try {
//   //   const { data } = await axiosInstance.get("user/token/refresh/");
//   //   localStorage.setItem("access", data.access_token);
//   //   req.headers.Authorization = `Bearer ${data.access_token}`;
//   // } catch (error: any) {
//   //   return (window.location.href = "/login");
//   // }
//   try {
//     const res = await fetch("http://localhost:8000/api/user/token/refresh/", {
//       credentials: "include",
//     });
//     const data = await res.json();
//     localStorage.setItem("access", data.access_token);
//     req.headers.Authorization = `Bearer ${data.access_token}`;
//   } catch (error: any) {
//     return (window.location.href = "/login");
//   }

//   return req;
// });

export default 10;
