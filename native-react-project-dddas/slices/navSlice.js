import { createSlice } from "@reduxjs/toolkit";
const initialState = {
    origin:null,
    destination:null,
    travelTimeInformation: null
}

export const navSlice = createSlice({
  name: 'nav',
  initialState,
  reducer:{
    setOrgin: (state, action) => {
        state.orgin = action.payload;
    },
    setDestination: (state,action) => {
        state.destination = action.payload;
    },
    setTravelTimeInformation: (state,action) => {
        state.travelTimeInformation = action.payload;
    },
},
});
export const {setOrgin, setDestination, setTravelTimeInformation } = navSlice.actions;

//Selectors
export const selectOrgin = (state) => state.nav.orgin;
export const selectDestination = (state) => state.nav.destination;
export const selectTravelTimeInformation = (state) => state.nav.travelTimeInformation;

export default navSlice.reducer;