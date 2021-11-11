import { combineReducers } from "redux";
import { demoReducer } from "./demoReducers";
import { userReducer } from "./userReducers";

const reducers = combineReducers({
  demo: demoReducer,
  user: userReducer,
});

const rootReducer = (state: any, action: any) => {
  switch (action.type) {
    case "RESET_STATE":
      return reducers(undefined, action);
    default:
      return reducers(state, action);
  }
};

// export default reducers;
export default rootReducer;
