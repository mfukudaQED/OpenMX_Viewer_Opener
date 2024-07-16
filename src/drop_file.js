function dropFile(element, fileContent, fileName) {
    const dataTransfer = new DataTransfer();
    
    const decodedContent = atob(fileContent);
    const file = new File([decodedContent], fileName);

    dataTransfer.items.add(file);

    element.dispatchEvent(new DragEvent('dragenter', { bubbles: true, dataTransfer }));
    element.dispatchEvent(new DragEvent('dragover', { bubbles: true, dataTransfer }));
    element.dispatchEvent(new DragEvent('drop', { bubbles: true, dataTransfer }));
}

// 引数として渡された要素とファイル内容、ファイル名で関数を呼び出す
const [element, fileContent, fileName] = arguments;
dropFile(element, fileContent, fileName);
