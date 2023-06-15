import { useState } from "react";
import { useForm } from "react-hook-form";
import Select from "react-select";
import { ToastContainer } from "react-toastify";
import { ApiMethods, ApiUrls } from "../../Shared/ApiUrls";
import { ToastNotification } from "../../Shared/constants";
import { options } from "../../Shared/constants";
import { useHistory } from "react-router-dom/cjs/react-router-dom.min";
const CreateCarAdmin = () => {
  const [loader, setLoader] = useState(false);
  const [carType, setCarType] = useState();
  const history = useHistory()
  const {
    register,
    handleSubmit,
    formState: { errors },
    reset,
  } = useForm();

  async function postCreateCarFn(payload, callback) {
    try {
      setLoader(true);
      const response = await fetch(ApiUrls.CREATE_CAR, {
        method: ApiMethods.POST,
        body: JSON.stringify(payload),
        headers: {
          access_token: `${localStorage.getItem("accesstoken")}`,
        },
      });
      const res = await response.json();

      if (response.status == 201 || response.status == 200) {
        callback("Post is created Succesfully", "success");
           // history.push('/allcars')
      } else if (response.status >= 400 || response.status <= 499) {
        callback(res.Message, "warn");
      } else {
        callback(res.Message, "warn");
      }
    } catch (err) {
      
      callback("Something went wrong", "error");
    } finally {
      setLoader(false);
    }
  }

  const submitHandler = (data) => {
   
    const payload = {
      brand: data.brand,
      model: data.model,
      registration_number: data.registration_number,
      power: data.power,
      type: carType?.value,
      price: data.price,
    };

    postCreateCarFn(payload, (message, type) => {
      ToastNotification(message, type);
      reset();
    });
  };

  return (
    <>
      <form onSubmit={handleSubmit(submitHandler)}>
        <div className="row mt-3">
          <div className="col-md-8 offset-2">
            <div className="card border-primary border-3">
              <div className="card-title m-auto text-primary ">
                <h4>CREATE CAR</h4>
                <hr />
              </div>
              <div className="card-body col-md-8 m-auto">
                <input
                  placeholder="Please enter registration number"
                  className=" form-control mt-2"
                  type="text"
                  {...register("registration_number", { required: true })}
                />
                {errors.registration_number && (
                  <p className=" text-danger">Please fill this field.</p>
                )}
                <input
                  placeholder="Please enter brand name"
                  className=" form-control mt-2"
                  type="text"
                  {...register("brand", { required: true })}
                />
                {errors.brand && (
                  <p className=" text-danger">Please fill this field.</p>
                )}
                <input
                  placeholder="Please enter model"
                  className=" form-control mt-2"
                  type="text"
                  {...register("model", { required: true })}
                />
                {errors.model && (
                  <p className=" text-danger">Please fill this field.</p>
                )}

                <input
                  placeholder="Please enter power"
                  className="form-control mt-2"
                  type="number"
                  {...register("power", { required: true })}
                />
                {errors.power && (
                  <p className="text-danger"> Please fill this field.</p>
                )}

                <Select
                 className=" mt-2"
                  onChange={(e) => {
                    setCarType(e);
                  }}
                  options={options}
                />

                <input
                  placeholder="Please enter price"
                  className="form-control mt-2"
                  type="number"
                  {...register("price", { required: true })}
                />
                {errors.price && (
                  <p className="text-danger"> Please fill this field.</p>
                )}
                <button
                  disabled={loader}
                  className="btn btn-primary mt-2"
                  type="submit"
                >
                  {loader ? "Creating..." : "Create Post"}
                </button>
              </div>
            </div>
          </div>
        </div>
        <ToastContainer />
      </form>
    </>
  );
};

export default CreateCarAdmin;
