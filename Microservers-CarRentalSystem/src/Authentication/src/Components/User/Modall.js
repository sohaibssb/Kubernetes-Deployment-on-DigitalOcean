import * as React from 'react';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import Modal from '@mui/material/Modal';
import { useForm } from "react-hook-form";

const style = {
  position: 'absolute' ,
  top: '50%',
  left: '50%',
  transform: 'translate(-50%, -50%)',
  width: 400,
  bgcolor: 'background.paper',
  border: '2px solid #000',
  boxShadow: 24,
  p: 4,
};

export default function BasicModal({handleClose , open , totalPrice , submitHandler , setStartDate,setEndDate , id}) {
 

    const {
        register,
        handleSubmit,
        formState: { errors },
        reset,
      } = useForm();

  return (
    <div>
      <Modal
        open={open}
        onClose={handleClose}
        aria-labelledby="modal-modal-title"
        aria-describedby="modal-modal-description"
      >
        <Box sx={style}>
          <Typography id="modal-modal-title" variant="h6" component="h2">
          Buy car on rent form
          </Typography>
          <Typography id="modal-modal-description" sx={{ mt: 2 }}>
          <form onSubmit={handleSubmit(submitHandler)}>
                <input
                  placeholder="Please enter registration number"
                  className=" form-control mt-2"
                  defaultValue={id}
                  type="text"
                  {...register("carUid", {
                    disabled: true,
                  })}
                />

                <input
                  placeholder="slect from date"
                  className=" form-control mt-2"
                  type="date"
                  {...register("dateFrom", {
                    required: true,
                    onChange: (e) => {
                      setStartDate(e.target.value);
                    },
                  })}
                />
                {errors.dateFrom && (
                  <p className=" text-danger">Please fill this field.</p>
                )}

                <input
                  placeholder="select to data"
                  className=" form-control mt-2"
                  type="date"
                  {...register("dateTo", {
                    required: true,
                    onChange: (e) => {
                      setEndDate(e.target.value);
                    },
                  })}
                />
                {errors.dateTo && (
                  <p className=" text-danger">Please fill this field.</p>
                )}


                <input
                  placeholder="total price"
                  className=" form-control mt-2"
                  defaultValue={totalPrice}
                  type="number"
                  {...register("totalprice", {
                    required: true,
                    disabled:true
                  })}
                />
                <button
                 
                  className="btn btn-primary mt-2"
                  type="submit"
                >
                  { "Buy on rent"}
                </button>
              </form>
          </Typography>
        </Box>
      </Modal>
    </div>
  );
}
