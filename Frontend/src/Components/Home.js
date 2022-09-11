// React imports
import React, { useState } from "react";
import FileBase64 from "react-file-base64";

const Home = () => {
  const [image, setImage] = useState("");
  const [updatedImage, setUpdatedImage] = useState("");

  const uploadImage = (e) => {
    e.preventDefault();
    callApi();
  };

  const callApi = async () => {
    try {
      const res = await fetch("http://127.0.0.1:8000/api/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ image: image.base64 }),
      });
      setUpdatedImage(await res.text());
    } catch (error) {
      alert(error);
    }
  };

  return (
    <div>
      <h1>Low Light Image Enhancement Using Deep Learning</h1>
      <br />
      <div>
        <form className="form">
          <label>Upload Image</label>
          <button className="btn">
            <FileBase64
              type="file"
              multiple={false}
              className="image-upload"
              onDone={(file) => setImage(file)}
            />
          </button>
          <button
            type="submit"
            className="btn btn-primary"
            onClick={uploadImage}
          >
            Submit
          </button>
        </form>
      </div>
      <br />
      <div
        className="container"
        style={{
          display: "flex",
          flexDirection: "row",
          justifyContent: "space-between",
        }}
      >
        <div>
          {image ? (
            <>
              <h1>Original Image</h1>
              <img src={image.base64} alt="original" />
              <br />
            </>
          ) : null}
        </div>
        <div>
          {updatedImage ? (
            <>
              <h1>New Image</h1>
              <img
                src={`data:image/png;base64,${updatedImage}`}
                alt="updated"
              />
              <br />
              <br />
              <a
                href={`data:image/png;base64,${updatedImage}`}
                download="low-light-enhanced.png"
              >
                <button className="btn btn-primary">Download</button>
              </a>
            </>
          ) : null}
        </div>
      </div>
    </div>
  );
};

export default Home;
