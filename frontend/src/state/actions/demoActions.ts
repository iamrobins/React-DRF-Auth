import { demoEnum } from "../enums";

export const demoOne = () => (dispatch: any) => {
  try {
    dispatch({ type: demoEnum.ONE });
  } catch (error: any) {
    console.log(error.message);
  }
};

export const demoTwo = () => (dispatch: any) => {
  try {
    dispatch({ type: demoEnum.TWO });
  } catch (error: any) {
    console.log(error.message);
  }
};
