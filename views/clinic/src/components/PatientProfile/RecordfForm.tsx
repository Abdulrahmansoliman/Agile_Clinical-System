import React, { useEffect, useState } from "react";
import { useForm, useFieldArray } from "react-hook-form";
import { DevTool } from "@hookform/devtools";
import "./styles/RecordForm.css";

interface ReportFormProps {
  id: number;
  entities: any;
}

interface ReportValues {
  report_attribute_id: number;
  id: number;
  report_entity_id: number;
  report_id: number;
  value: string;
  value_name: string;
}

interface Report {
  entity_name: string;
  id: number;
  record_id: number;
  report_entity_id: number;
  values: ReportValues[];
}

interface RecordFormData {
  id: number;
  notes: string;
  patient_profile_id: number;
  date: string;
  doctor_id: number;
  marital_status: string;
  reports: Report[];
}

const RecordForm: React.FC<ReportFormProps> = ({ id, entities }) => {
  const [showRecordForm, setShowRecordForm] = useState(false);
  const [newEntity, setNewEntity] = useState(false);

  function renderEntities(entityId: number) {
    const entity = entities.find((entity: any) => entity.id === entityId);
    if (entity) {
      return (
        <div>
          <label>{entity.name}</label>
          {entity.attributes.map((a: any) => {
            return (
              <div>
                <label>{a.name}</label>
                <input type="text" />
              </div>
            );
          })}
        </div>
      );
    } else {
      return null; // or you can display an error message
    }
  }
  const form = useForm<RecordFormData>({
    defaultValues: {
      id: 0,
      notes: "",
      patient_profile_id: id,
      date: "",
      doctor_id: 0,
      marital_status: "",
      reports: [],
    },
  });
  const { register, control, handleSubmit, formState, reset } = form;
  const { errors, isSubmitSuccessful } = formState;

  const { fields, append, remove } = useFieldArray({
    name: "reports",
    control,
  });

  const handleAddRecord = () => {
    setShowRecordForm(!showRecordForm);
  };

  const handleAddReport = (fieldID: number, entityId: number) => {
    console.log("Field ID: ", fieldID);
    console.log("Fields: ", fields);
    while (fields[fieldID].values.length > 0) {
      fields[fieldID].values.pop();
    }
    console.log(entities[entityId - 1].attributes);
    entities[entityId - 1].attributes.map((a: any) => {
      fields[fieldID].values.push({
        report_attribute_id: a.id,
        id: 0,
        report_entity_id: entityId - 1,
        report_id: 0,
        value: "",
        value_name: "",
      });
    });
    console.log("Fields: ", fields[fieldID].values);
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
                onClick={() =>
                  append({
                    entity_name: "",
                    id: 0,
                    record_id: 0,
                    report_entity_id: 0,
                    values: [],
                  })
                }
              >
                Add Report
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
            <div>
              <label>Reports:</label>
              <div>
                {fields.map((field, index) => (
                  <div key={field.id}>
                    <label>Select entity_name</label>
                    <select
                      {...register(`reports.${index}.entity_name` as const, {
                        required: "Please select an entity",
                      })}
                      onChange={(e) => {
                        handleAddReport(index, parseInt(e.target.value));
                        append({
                          entity_name: "",
                          id: 0,
                          record_id: 0,
                          report_entity_id: 0,
                          values: [],
                        });
                        remove(fields.length);
                      }}
                    >
                      <option value="">Select an entity</option>
                      {entities.map((entity: any) => (
                        <option key={entity.id} value={entity.id}>
                          {entity.name}
                        </option>
                      ))}
                    </select>
                    <button type="button" onClick={() => remove(index)}>
                      Remove
                    </button>
                    {fields[index].values.map((value, index2) => (
                      <div key={value.id}>
                        <label>
                          {
                            entities.find(
                              (entity: any) =>
                                entities.indexOf(entity) ===
                                value.report_entity_id
                            ).attributes[index2].name
                          }
                        </label>
                        <input
                          {...register(
                            `reports.${index}.values.${index2}.value` as const,
                            {
                              required: {
                                value: true,
                                message: "Don't forget to add value",
                              },
                            }
                          )}
                        />
                      </div>
                    ))}
                  </div>
                ))}
              </div>
            </div>
            <br />
            <div className="buttonDown">
              <div>
                <button type="submit">Submit</button>
                <button type="button" onClick={() => reset()}>
                  Reset
                </button>
              </div>
              <div>
                <button onClick={handleAddRecord}>Close</button>
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
