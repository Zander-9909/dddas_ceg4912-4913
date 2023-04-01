import React from 'react';
import { createStackNavigator } from '@react-navigation/stack';
import SettingsScreen from '../screens/SettingsScreen';

import CameraOutput from '../screens/SettingsComponents/CameraOutput';
import Global from './Global';
import OuterNavigator from './OuterNavigator';

const Stack = createStackNavigator();

function SettingsNavigator() {
    return (
        <Stack.Navigator
            screenOptions={{}}
            initialRouteName={Global.settingsName}>

            <Stack.Screen name={Global.settingsName}
                component={SettingsScreen}
                options={{
                    headerShown: false,
                    title: 'Settings',
                }}
            />
            <Stack.Screen name={Global.cameraOutputName} 
            component={CameraOutput} 
            options={{
                title: 'Facial Detection'
            }}
            />
            <Stack.Screen name={Global.outerName}
            component={OuterNavigator} 
            options={{
                headerShown: false, // hide the top bar when navigating from outer to inner
                gestureEnabled: false // cannot swipe back from inner to outer navigations
            }}/>

        </Stack.Navigator>
    );
}

export default SettingsNavigator;
