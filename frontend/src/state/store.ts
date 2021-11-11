import { createStore, applyMiddleware } from "redux";
import { composeWithDevTools } from "redux-devtools-extension";
import reducers from "./reducers";
import thunk from "redux-thunk";

const initialState = {};

const middlewares: any = [thunk]; //Put middlewares here

export const store = createStore(
  reducers,
  initialState,
  composeWithDevTools(applyMiddleware(...middlewares))
);
