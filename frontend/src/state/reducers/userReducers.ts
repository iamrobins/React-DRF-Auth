import { userEnum } from "../enums";

export const userReducer = (state = { user: null }, action: any) => {
  switch (action.type) {
    case userEnum.SAVE_USER:
      return { user: action.payload };
    default:
      return state;
  }
};
