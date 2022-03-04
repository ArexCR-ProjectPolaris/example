%% First Steps

% 1) Download Valispace Matlab Toolbox from github: https://github.com/valispace/ValispaceMatlabToolbox
% 2) Double-click to install (regardless of platform)
% 3) Please review the Usage section of this repository for API instructions

%% Initializing Valispace API

% Project url
url = "https://polarisproject.valispace.com";
% Your username and password
% NOTE: ensure that your username and password are never saved or pushed to the repo
% Note: You may wish to store your username here for testing. You can then
% replace the input with that variable username
% username = "";
% Warning: I highly recommend that you never store your password here.

% Login to Valispace API
ValispaceInit(url, input("Enter valispace username: "), input("Enter valispace password: "));
% Recommended: pull all valis for faster access or access via name
if ~exist('allValis', 'var')
    allValis = ValispacePull();
end

%% Setting up Variables from Valis

% Getting Value by ID or Name
powerByID = ValispaceGetValue(19924);
% Note: if you get a vali by name, it must be written exactly how it is represented in valispace
powerByName = ValispaceGetValue("Motor.Power");

% To make a struct in Matlab, you make define everything at once:
valiStruct1 = struct("Power", ValispaceGetValue(19924), "mdot", ValispaceGetValue(19912), "T0", ValispaceGetValue(19902), "MM", ValispaceGetValue(19898));
% Or, you may define an empty struct and individual components:
valiStruct2 = struct;
valiStruct2.power = ValispaceGetValue(19924);
valiStruct2.mdot = ValispaceGetValue(19912);
valiStruct2.T0 = ValispaceGetValue(19902);
valiStruct2.MM =  ValispaceGetValue(19898);
% You may also keep it simple and just define variables:
power = ValispaceGetValue(19924);
mdot = ValispaceGetValue(19912);
T0 = ValispaceGetValue(19902);
MM =  ValispaceGetValue(19898);

% In short, just keep it organized


%% Processing
% Here is where I'd like to note that the original tutorial in Python is
% not feasible in Matlab. While it may be possible to recreate it, it is
% simply too difficult for a tutorial. Also, Python is the selected main
% language and Matlab should only be used in approved cases (please verify
% your case with your Programming Coordinator and/or the Head of 
% Informatics). As always, use good programming practices and comment well.
% I don't know code that I didn't write, and that's how it should be
% reviewed.

%% Updating Valis with Local Variables
% You may update a variable by ID or exact name:
ValispacePushValue(19924, power);
ValispacePushValue("Motor.Power", power);
% Note: Matlab cannot create valis, they must be made on Valispace
% Warning: Use of the REST API, as shown in points 7 & 8 of the
% documentation, is prohibited. Please use only the methods defined in
% points 1-6
