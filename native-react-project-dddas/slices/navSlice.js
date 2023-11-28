import { createSlice } from "@reduxjs/toolkit";

const initialState = {
    origin: null,
    destination: null,
    waypoint: null,
    travelTimeInformation: null
}

export const navSlice = createSlice({
    name: 'nav',
    initialState: initialState,
    reducers: {
        setOrigin: (state, action) => {
            state.origin = action.payload;
        },
        setDestination: (state, action) => {
            state.destination = action.payload;
        },
        setWaypoint: (state, action) => {
            state.waypoint = action.payload;
        },
        setTravelTimeInformation: (state, action) => {
            state.travelTimeInformation = action.payload;
        },
    },
});

export const { setOrigin, setDestination, setWaypoint, setTravelTimeInformation } = navSlice.actions;


// Selectors
export const selectOrigin = (state) => state.nav.origin;
export const selectDestination = (state) => state.nav.destination;
export const selectWaypoint = (state) => state.nav.waypoint;
export const selectTravelTimeInformation = (state) => state.nav.travelTimeInformation


export default navSlice.reducer;