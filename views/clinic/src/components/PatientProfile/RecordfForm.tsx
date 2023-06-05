import React, { useEffect, useState } from "react";
import { useForm, useFieldArray } from "react-hook-form";
import "./styles/RecordForm.css";

interface ReportFormProps {
  id: number;
  entities: any;
}

interface ReportValues {
  report_attribute_id: number;
  report_entity_id: number;
  value: string;
}

interface Report {
  entity_name: string;
  report_entity_id: number;
  values: ReportValues[];
}

interface RecordFormData {
  notes: string;
  patient_profile_id: number;
  date: string;
  doctor_id: number;
  marital_status: string;
  reports: Report[];
}

const RecordForm: React.FC<ReportFormProps> = ({ id, entities }) => {
  const [showRecordForm, setShowRecordForm] = useState(false);

  const form = useForm<RecordFormData>({
    defaultValues: {
      notes: "",
      patient_profile_id: id,
      date: new Date().toISOString().split("T")[0],
      doctor_id: 3,
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
    fields[fieldID].report_entity_id = entityId;
    console.log("Fields: ", fields[fieldID].report_entity_id);

    console.log(entities[entityId - 1].attributes);

    while (fields[fieldID].values.length > 0) {
      fields[fieldID].values.pop();
    }

    entities[entityId - 1].attributes.map((a: any) => {
      fields[fieldID].values.push({
        report_attribute_id: a.id,
        report_entity_id: entityId,
        value: "",
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
    form.getValues().reports.map((report: any) => {
      let newid = report.values[0].report_entity_id;
      report.report_entity_id = newid;
    });

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
                    <label>Select report</label>
                    <select
                      {...register(`reports.${index}.entity_name` as const, {
                        required: "Please select an entity",
                      })}
                      onChange={(e) => {
                        handleAddReport(index, parseInt(e.target.value));

                        append({
                          entity_name: "",
                          report_entity_id: parseInt(e.target.value),
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
                      <div key={index2}>
                        <label>
                          {
                            entities.find(
                              (entity: any) =>
                                entities.indexOf(entity) ===
                                value.report_entity_id
                            )?.attributes[index2]?.name
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
        </div>
      )}
    </div>
  );
};

export default RecordForm;
