% Muhammad Maulud Hidayatullah Rambe | 1301154166
% Chando Anggara Natanael Batubara | 1301154390
% S1 Teknik Informatika, Fakultas Informatika, Telkom University 2018

clear; clc;

sim1ser = importfile('Server-1.txt', 1, 10);
sim2ser = importfile('Server-2.txt', 1, 10);
sim3ser= importfile('Server-3.txt', 1, 10);
sim4ser= importfile('Server-4.txt', 1, 10);
sim5ser = importfile('Server-5.txt', 1, 10);

numofsim_1 = sim1ser(:, 1);
arrofavgwait_1 = sim1ser(:, 2);
arrofavgqueue_1 = sim1ser(:, 3);

numofsim_2 = sim2ser(:, 1);
arrofavgwait_2 = sim2ser(:, 2);
arrofavgqueue_2 = sim2ser(:, 3);

numofsim_3 = sim3ser(:, 1);
arrofavgwait_3 = sim3ser(:, 2);
arrofavgqueue_3 = sim3ser(:, 3);

numofsim_4 = sim4ser(:, 1);
arrofavgwait_4 = sim4ser(:, 2);
arrofavgqueue_4 = sim4ser(:, 3);

numofsim_5 = sim5ser(:, 1);
arrofavgwait_5 = sim5ser(:, 2);
arrofavgqueue_5 = sim5ser(:, 3);

total_numofsim = 1:50;
total_arrofavgwait = [arrofavgwait_1 arrofavgwait_2 arrofavgwait_3 arrofavgwait_4 arrofavgwait_5];
total_arrofavgwait = total_arrofavgwait(:);
total_arrofavgqueue = [arrofavgqueue_1 arrofavgqueue_2 arrofavgqueue_3 arrofavgqueue_4 arrofavgqueue_5];
total_arrofavgqueue = total_arrofavgqueue(:);

% 
% Combined Plot
% 
figComb = figure('name', 'Bank Service Problem', 'NumberTitle', 'off');
panComb = uipanel('Parent',figComb,'BorderType','none'); 
panComb.Title = 'Bank Service Simulation'; 
panComb.TitlePosition = 'centertop'; 
panComb.FontSize = 12;
panComb.FontWeight = 'bold';

subplot(1, 1, 1, 'Parent', panComb)
plot(total_numofsim, total_arrofavgwait, total_numofsim, total_arrofavgqueue);
title('Number of Server: 1 - 5');
ylabel('Averages (Minutes)');
xlabel('Number of Simulation (increase server every 10 simulation)');
legend('avgWaitTime', 'avgQueueLength');


% 
% Individual Plot
% 
fig = figure('name', 'Bank Service Problem', 'NumberTitle', 'off');
pan = uipanel('Parent',fig,'BorderType','none'); 
pan.Title = 'Bank Service Simulation'; 
pan.TitlePosition = 'centertop'; 
pan.FontSize = 12;
pan.FontWeight = 'bold';

subplot(1, 5, 1, 'Parent', pan)
plot(numofsim_1, arrofavgwait_1, numofsim_1, arrofavgqueue_1);
title('Number of Server: 1');
ylabel('Averages (Minutes)');
xlabel('Simulation Number');

subplot(1, 5, 2, 'Parent', pan)
plot(numofsim_2, arrofavgwait_2, numofsim_2, arrofavgqueue_2);
title('Number of Server: 2');
xlabel('Simulation Number');

subplot(1, 5, 3, 'Parent', pan)
plot(numofsim_3, arrofavgwait_3, numofsim_3, arrofavgqueue_3);
title('Number of Server: 3');
xlabel('Simulation Number');

subplot(1, 5, 4, 'Parent', pan)
plot(numofsim_4, arrofavgwait_4, numofsim_4, arrofavgqueue_4);
title('Number of Server: 4');
xlabel('Simulation Number');

subplot(1, 5, 5, 'Parent', pan)
plot(numofsim_5, arrofavgwait_5, numofsim_5, arrofavgqueue_5);
title('Number of Server: 5');
legend('avgWaitTime', 'avgQueueLength');
xlabel('Simulation Number');