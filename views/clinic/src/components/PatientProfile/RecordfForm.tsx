import React, { useEffect, useState } from "react";
import { useForm, useFieldArray } from "react-hook-form";
import { DevTool } from "@hookform/devtools";
import "./styles/RecordForm.css";

interface RecordFormProps {
  id: number;
}

interface RecordFormData {
  id: number;
  notes: string;
  patient_profile_id: number;
  date: string;
  doctor_id: number;
  marital_status: string;
  lab_tests: {
    test: string;
    results: string;
    date: string;
  }[];
  medications: {
    med: string;
    notes: string;
  }[];
}

const RecordForm: React.FC<RecordFormProps> = ({ id }) => {
  const [showRecordForm, setShowRecordForm] = useState(false);

  const form = useForm<RecordFormData>({
    defaultValues: {
      id: 0,
      notes: "",
      patient_profile_id: id,
      date: "",
      doctor_id: 0,
      marital_status: "",
      lab_tests: [
        {
          test: "",
          results: "",
          date: "",
        },
      ],
      medications: [
        {
          med: "",
          notes: "",
        },
      ],
    },
  });
  const { register, control, handleSubmit, formState, reset } = form;
  const { errors, isSubmitSuccessful } = formState;

  const {
    fields: labtestField,
    append: addLabTest,
    remove: removeLabTest,
  } = useFieldArray({
    name: "lab_tests",
    control,
  });
  const {
    fields: medicationField,
    append: addMedication,
    remove: removeMedication,
  } = useFieldArray({
    name: "medications",
    control,
  });

  const handleAddRecord = () => {
    setShowRecordForm(!showRecordForm);
  };

  useEffect(() => {
    if (isSubmitSuccessful) {
      reset();
    }
  }, [isSubmitSuccessful, reset]);

  const onSubmit = (data: RecordFormData) => {
    console.log("Record Form Data: ", form.getValues());
    setShowRecordForm(!showRecordForm);
    fetch("http://localhost:5000/records", {
      method: "POST",
      mode: "no-cors",
      body: JSON.stringify(form.getValues()),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log("Success:", data);
      });
  };

  return (
    <div>
      <button onClick={handleAddRecord}>Add Record</button>
      {showRecordForm && (
        <div className="containerForm">
          <div className="FormHead">
            <h3>Record Form</h3>
            <div>
              <button
                type="button"
                onClick={() => addLabTest({ test: "", results: "", date: "" })}
              >
                Add test
              </button>
              <button
                type="button"
                onClick={() => addMedication({ med: "", notes: "" })}
              >
                Add med
              </button>
            </div>
          </div>
          <form onSubmit={handleSubmit(onSubmit)} noValidate>
            <label>
              Notes:
              <input
                id="notes"
                {...register("notes", {
                  required: {
                    value: true,
                    message: "Don't forget to add Notes",
                  },
                })}
              ></input>
              <p className="error">{errors.notes?.message}</p>
            </label>
            <br />
            <label>
              Marital Status:
              <input
                list="martial"
                type="text"
                {...register("marital_status", {
                  required: {
                    value: true,
                    message: "Don't forget to add Marital Status",
                  },
                })}
              />
              <datalist id="martial">
                <option value="Married" />
                <option value="Engaged" />
                <option value="Divorced" />
              </datalist>
              <p className="error"> {errors.marital_status?.message}</p>
            </label>
            <br />
            <label>list of lab tests:</label>
            <div>
              {labtestField.map((f, index) => {
                return (
                  <div key={f.id}>
                    <label>Test:{index + 1}</label>
                    <label>Test type:</label>
                    <input
                      type="text"
                      {...register(`lab_tests.${index}.test` as const)}
                    />
                    <label>Results:{index + 1}</label>
                    <input
                      type="text"
                      {...register(`lab_tests.${index}.results` as const)}
                    />
                    <button type="button" onClick={() => removeLabTest(index)}>
                      Remove
                    </button>
                  </div>
                );
              })}
            </div>
            <br />
            <label>list of medication:</label>
            <div>
              {medicationField.map((f, index) => {
                return (
                  <div key={f.id}>
                    <label>Medication:{index + 1}</label>
                    <label>Medication type:</label>
                    <input
                      type="text"
                      {...register(`medications.${index}.med` as const)}
                    />
                    <label>Notes:{index + 1}</label>
                    <input
                      type="text"
                      {...register(`medications.${index}.notes` as const)}
                    />
                    <button
                      type="button"
                      onClick={() => removeMedication(index)}
                    >
                      Remove
                    </button>
                  </div>
                );
              })}
            </div>
            <div className="buttonDown">
              <div>
                <button type="submit">Submit</button>
                <button type="button" onClick={() => reset()}>
                  reset
                </button>
              </div>
              <div>
                <button onClick={handleAddRecord}> close</button>
              </div>
            </div>
          </form>
          <DevTool control={control} />
        </div>
      )}
    </div>
  );
};

export default RecordForm;
