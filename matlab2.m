function render_images()
    % Assuming the image size is known
    image_size = [256, 256];

    % Read the data from the text files and reshape
    matlab1_data = reshape(dlmread('matlab1_output.txt'), image_size);
    c_data = reshape(dlmread('c_output.txt'), image_size);
    haskell_data = reshape(dlmread('haskell_output.txt'), image_size);
    prolog_data = reshape(dlmread('prolog_output.txt'), image_size);

    % Display the images side by side
    fig = figure('Name', 'Image Processing Results', 'NumberTitle', 'off', 'WindowStyle', 'modal');
    subplot(2,2,1), imshow(matlab1_data, []), title('Original Image');
    subplot(2,2,2), imshow(c_data, []), title('Black and White with C');
    subplot(2,2,3), imshow(haskell_data, []), title('Color Flipped with Haskell');
    subplot(2,2,4), imshow(prolog_data, []), title('Rotated with Prolog');

    % Bring figure to front and keep it open until the user closes it
    figure(fig);
    disp('Close the figure window to continue.');
    waitfor(fig);
end
