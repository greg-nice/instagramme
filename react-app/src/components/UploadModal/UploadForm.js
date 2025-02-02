import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { createPost } from "../../store/posts";
import "./UploadModal.css";
import media from "./images/media.png";
import DisplayForm from "./DisplayForm";

function UploadForm({ hideForm }) {
  const sessionUser = useSelector((state) => state.session.user);
  const user_id = sessionUser.id;
  const dispatch = useDispatch();
  const [file, setFile] = useState(null);
  const [preview, setPreview] = useState();
  const [description, setDescription] = useState("");
  const [url, setUrl] = useState("");
  const [errors, setErrors] = useState([]);

  useEffect(() => {
    if (!file) {
      setPreview(undefined);
      return;
    }
    const objectUrl = URL.createObjectURL(file);
    setPreview(objectUrl);
    return () => URL.revokeObjectURL(objectUrl);
  }, [file]);

  const handleFile = (e) => {
    setFile(e.target.files[0]);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    let newErrors = [];
    dispatch(createPost({ user_id, description, file }))
      .then(() => {
        setDescription("");
        setUrl("");
      })
      .catch(async (res) => {
        const data = await res.json();
        if (data && data.errors) {
          newErrors = data.errors;
          setErrors(newErrors);
        }
      });
  };

  if (file) {
    return (
      <>
        <DisplayForm preview={preview} file={file} hideForm={hideForm} />
      </>
    );
  }

  return (
    <div className="uploadFormMain">
      <div className="uploadFormTop">
        <p>Create new post</p>
      </div>
      <div className="uploadFormSpacer">
        {file && <img src={preview} alt="" />}
      </div>
      <div className="uploadFormBtm">
        <div className="mediaImgContainer">
          <img src={media} alt="" className="mediaImg"></img>
        </div>
        <div className="uploadTextContainer">
          <p>Upload photos here</p>
        </div>
        <div>
          <form
            className="formContainer"
            onSubmit={handleSubmit}
            className="form"
          >
            <div className="buttonWrapper">
              <input type="file" id="fileUpload" onChange={handleFile} />
              <label htmlFor="fileUpload" className="fileUploadBtn">
                Select from Computer
              </label>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
}

export default UploadForm;