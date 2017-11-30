%Lander project
clc;
clear;
printf("Lunar Lander version 1.0\n")
printf("**************************")

%Random whole number altitude between 0-100:
x_0=ceil(10*rand(1))+90;
v_0 = rand(1); %Initial velocity in meter/second
%Ma=0.1;
%gamma=1.3;
%R=8.314*10^3;
%Te=600;
%ve = Ma*sqrt(gamma * R * Te) %Ma: Mach number, gamma: cp/cv, R: gas constant, Te: absolute temperature of motor 
ve=1.;
grav=1.63; %Acceleration due to gravity in m/sq.s
mass = 1000*10^3; %Mass in kilogram
mass_fuelTotal = 75; %Initial total mass of fuel in kg
friction = 0; %Friction

printf("\n\n")
printf("You need to land your shuttle (don't crash it.. or you lose your job... and your life probably..)\n")
printf("\n\n")
printf("Control the thrust by providing a value for the amount of fuel you wish to burn and the burn time\n")
printf("Remember that you have limited fuel...\n")      
printf("\n\n")
printf("Your starting altitude is %1.2f meter above the m\n", x_0)
printf("Your current velocity is %1.3f meter/second\n", v_0)
printf("The gravitational acceleration is %1.3f meter/sq.second \n", grav)
printf("The shuttle has a mass of %d [kg] and has an initial fuel mass of %1.3f\n [kg] \n\n", mass, mass_fuelTotal)

%User input and loop
x_now=x_0;
v_now=v_0;
x_values=[];
instance=0;
while(x_now>=0)
  m_burn = input("Enter mass of fuel you wish to burn [kg]: "); %User input
  burn_time = input("Enter burn time [second]: "); %User input
  t=burn_time;
  mdot = m_burn/t;
  printf("Current fuel consumption rate is %1.3f [kg/s] \n", mdot)
    if(instance==0)
      m_now = mass+mass_fuelTotal-m_burn;
    else
      m_now = m_prev - m_burn;  
    endif
  x_prev = x_now;
  v_prev = v_now;
  
  x_next = -0.5*grav*t^2 + mdot*ve*t^2/(2*m_now) + v_prev*t + x_prev; %Position at time  
  v_next =  -grav*t + (mdot/m_now)*ve*t + v_prev; %velocity at time 
  
  m_prev=m_now;
    if(instance==0)
      m_fuel_now = mass_fuelTotal-m_burn;
      printf("Current altitude is %1.3f and the amount of fuel left is %1.3f\n", x_next, m_fuel_now)
    else
      m_fuel_now = m_fuel_prev - m_burn  ;
      printf("Current altitude is %1.3f and the amount of fuel left is %1.3f\n", x_next, m_fuel_now)
    endif  
  instance=1;    
  x_now = x_next;
  v_now = v_next;
  m_fuel_prev = m_fuel_now;
  x_values = [x_values, x_now];
  
  
    if((m_fuel_now==0 && x_now > 0) || m_fuel_now<0 || x_now<0)
     printf("CRASH!\n\n");
     pause(0.3)
     printf("Following is your trajectory report\n\n")
     plot(x_values, 'r*')
     title("Descent")
    endif
endwhile  


 if(x_now==0)
  printf("Landed!")
 endif

  



