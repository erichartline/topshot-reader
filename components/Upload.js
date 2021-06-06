import React from "react"

const getFormData = (file) => {
  const formData = new FormData()
  formData.append("csv", file)
  return formData
}

const Upload = () => {
  const [file, setFile] = React.useState(null)

  const handleChange = (event) => {
    setFile(event.target.files[0])
  }

  const handleFileUpload = async () => {
    if (!file) return

    const formData = new FormData()
    formData.append("csv", file)

    try {
      const res = await fetch(`/api/upload`, {
        method: "POST",
        body: getFormData(file),
      })
      console.log(res)
    } catch (error) {
      console.log(error)
    }
  }

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
    </div>
  )
}

export default Upload
