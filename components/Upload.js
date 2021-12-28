import React from "react";

const getFormData = (file) => {
  const formData = new FormData();
  formData.append("csv", file);
  return formData;
};

const Upload = () => {
  const [file, setFile] = React.useState(null);
  const [error, setError] = React.useState(false);

  const handleChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleFileUpload = async () => {
    if (!file) return;

    const formData = new FormData();
    formData.append("csv", file);

    try {
      const res = await fetch(`/api/upload`, {
        method: "POST",
        body: getFormData(file),
      });
      if (res.status !== 200) {
        setError(true);
      }
      console.log(res);
    } catch (error) {
      console.log(error);
      setError(true);
    }
  };

  return (
    <div>
      <h1>File Upload</h1>
      <input
        type="file"
        id="file-upload"
        name="file-input"
        onChange={handleChange}
      />
      <button disabled={!file} onClick={handleFileUpload}>
        Upload
      </button>
      {error && <div>got an error :(</div>}
    </div>
  );
};

export default Upload;
