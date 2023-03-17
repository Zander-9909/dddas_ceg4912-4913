import * as React from 'react';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import Ionicons from 'react-native-vector-icons/Ionicons'

// screens
import NavigationScreen from '../screens/NavigationScreen';
import AlertsScreen from '../screens/AlertsScreen';
import StatsScreen from '../screens/StatsScreen';
import SettingsScreen from '../screens/SettingsScreen';

// screen names
const navigationName = 'Navigation';
const alertsName = 'Alerts';
const statsName = 'Stats';
const settingsName = 'Settings'

const Tab = createBottomTabNavigator();

function InnerNavigator() {
    return (
        <Tab.Navigator
            initialRouteName={navigationName}
            screenOptions={({ route }) => ({
                // tab bar style
                headerShown: false, // hides header
                tabBarActiveTintColor: 'tomato',
                tabBarInactiveTintColor: 'grey',

                // tab bar icon select
                tabBarIcon: ({ focused, color, size }) => {
                    let iconName;
                    let rn = route.name;
                    // https://ionic.io/ionicons/
                    switch (rn) {
                        case navigationName:
                            iconName = focused ? 'home' : 'home-outline';
                            break;
                        case alertsName:
                            iconName = focused ? 'list' : 'list-outline';
                            break;
                        case statsName:
                            iconName = focused ? 'stats-chart' : 'stats-chart-outline';
                            break;
                        case settingsName:
                            iconName = focused ? 'settings' : 'settings-outline';
                            break;
                    }
                    return <Ionicons name={iconName} size={size} color={color} />

                },
            })}>

            <Tab.Screen name={navigationName} component={NavigationScreen} />
            <Tab.Screen name={alertsName} component={AlertsScreen} />
            <Tab.Screen name={statsName} component={StatsScreen} />
            <Tab.Screen name={settingsName} component={SettingsScreen} />

        </Tab.Navigator>
    );
}

export default InnerNavigator;
