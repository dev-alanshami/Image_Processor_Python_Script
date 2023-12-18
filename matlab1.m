% Read the path from 'path.txt'
fileID = fopen('path.txt', 'r');
image_path = fgets(fileID);
fclose(fileID);

% Read the image
imdata = imread(image_path);      % Read the image data
imdata_id = reshape(imdata, 1, []);   % Reshape the image data into a 1D array

% Write the data to 'ml1_input.txt' using space as the delimiter
writematrix(imdata_id, 'matlab1_output.txt', 'Delimiter', ' ');
