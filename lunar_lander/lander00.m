%Lander project

clc;
clear;
%altitude_0 = 100; %Initial altitude in meter
%Random whole number altitude between 0-100:
altitude_0=ceil(100*rand(1));
velocity_0 = 0.1; %Initial velocity in meter/second
Ma=0.1;
gamma=1.3;
R=8.314*10^3;
Te=600;
velocity_motor = Ma*sqrt(gamma * R * Te) %Ma: Mach number, gamma: cp/cv, R: gas constant, Te: absolute temperature of motor 
grav=1.63; %Acceleration due to gravity in m/sq.s
mass = 1000*10^3; %Mass in kilogram
mass_fuelTotal = 2500; %Initial total mass of fuel in kg
friction = 0; %Friction

printf("\n\n")
printf("You need to land your shuttle (don't crash it.. or you lose your job... and your life probably..)\n")
printf("\n\n")
printf("Control the thrust by providing a value for the amount of fuel you wish to burn and the burn time\n")
printf("Remember that you have limited fuel...\n")      
printf("\n\n")
printf("Your starting altitude is %1.2f meter above the planet\n", altitude_0)
printf("Your current velocity is %1.3f meter/second\n", velocity_0)
printf("The gravitational acceleration is %1.3f meter/sq.second \n", grav)
printf("The shuttle has a mass of %d tonne and has an initial fuel mass of %1.3f\n kilogram \n\n", mass, mass_fuelTotal)

%User input and loop
altitude_now=altitude_0;
velocity_now=velocity_0;
%while(altitude_now<=0)
  m_burn = input("Enter mass of fuel you wish to burn [kg]: "); %User input
  burn_time = input("Enter burn time [second]: "); %User input
  t=burn_time;
  printf("Current fuel consumption rate is %1.3f [kg/s] \n", m_burn/burn_time)
  m = mass+mass_fuelTotal-m_burn;
  %  M = m_burn/m; %In case some ratio is necessary
  x0 = altitude_now;
  v0 = velocity_now;
  mfdot = m_burn/burn_time;
  
  x_next = (grav*m^2)/mfdot^2 - (exp(-((mfdot*t)/m))*grav*m^2)/mfdot^2 - (grav*m*t)/mfdot + (m*v0)/mfdot - (exp(-((mfdot*t)/m))*m*v0)/mfdot + x0; %Position at time 
 
  v_next = -((grav*m)/mfdot) + (exp(-((mfdot*t)/m))*grav*m)/mfdot + exp(-((mfdot*t)/m))*v0; %velocity at time 
  
  altitude_temp = x_next
  
%endwhile  



