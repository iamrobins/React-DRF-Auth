import { userEnum } from "../enums";

export const saveUser = (user: any) => (dispatch: any) => {
  dispatch({ type: userEnum.SAVE_USER, payload: user });
};
