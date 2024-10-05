
        // Initialize Fabric.js canvas
        const canvas = new fabric.Canvas('canvas');

        var border = new fabric.Rect({
            left: 0,
            top: 0,
            width: canvas.width,
            height: canvas.height,
            fill: 'transparent',      // No fill
            stroke: 'black',          // Border color
            strokeWidth: 2,           // Border width
            selectable: false,        // Cannot be selected
            evented: false            // No mouse events
          });
        
          // Add the border rectangle to the canvas and move it to the back
          canvas.add(border);
          canvas.sendToBack(border);
        

        // Set initial drawing state
        let isDrawing = false;
        let isErasing = false;

        // Enable drawing on the canvas
        document.getElementById('drawBtn').addEventListener('click', () => {
            isErasing = false;
            canvas.isDrawingMode = true;
            canvas.freeDrawingBrush.width = 5; // Set brush width
            canvas.freeDrawingBrush.color = 'red'; // Set brush color
        });

        // Enable erasing on the canvas
        document.getElementById('eraseBtn').addEventListener('click', () => {
            isErasing = true;
            canvas.isDrawingMode = true; // Still in drawing mode for erasing
            canvas.freeDrawingBrush.width = 10; // Set brush width for eraser
            canvas.freeDrawingBrush.color = '#fff'; // Set brush color to white for erasing
        });

        // Clear the canvas
        document.getElementById('clearBtn').addEventListener('click', () => {
            // Instead of canvas.clear(), remove only the objects
            canvas.getObjects().forEach((obj) => {
                if (obj !== canvas.backgroundImage) {
                    canvas.remove(obj);
                }
            });
            canvas.renderAll();  // Redraw the canvas

        });

        // Prevent mouse events when not in drawing or erasing mode
        canvas.on('mouse:up', () => {
            if (isErasing) {
                canvas.isDrawingMode = false; // Disable drawing mode after erasing
            }
        });