import { useEffect, useState } from "react";
import { createRecord, getRecords, updateRecord, deleteRecord } from "./api";

const DATABASES = {
  customers: {
    title: "Customers",
    columns: [
      { key: "id", label: "ID" },
      { key: "name", label: "Name" },
      { key: "email", label: "Email" },
      { key: "phone", label: "Phone" }
    ],

    fields: [
      {
        key: "name",
        label: "Name",
        type: "text"
      },
      {
        key: "email",
        label: "Email",
        type: "email"
      },
      {
        key: "phone",
        label: "Phone",
        type: "text"
      }      
    ],

    emptyRecord: {
      name: "",
      email: "",
      phone: ""
    }
  },

  vehicles: {
    title: "Vehicles",
    columns: [
      { key: "id", label: "ID" },
      { key: "registration_number", label: "Registration Number" },
      { key: "manufacturer", label: "Manufacturer" },
      { key: "model", label: "Model" },
      { key: "year", label: "Year" },
      { key: "customer_id", label: "Customer ID" }
    ],

    fields: [
      {
        key: "registration_number",
        label: "Registration Number",
        type: "text"
      },
      {
        key: "manufacturer",
        label: "Manufacturer",
        type: "text"
      },
      {
        key: "model",
        label: "Model",
        type: "text"
      },
      {
        key: "year",
        label: "Year",
        type: "number"
      },
      {
        key: "customer_id",
        label: "Customer ID",
        type: "number"
      }
    ],

    emptyRecord: {
      registration_number: "",
      manufacturer: "",
      model: "",
      year: "",
      customer_id: ""
    }
  },

  services: {
    title: "Services",
    columns: [
      { key: "id", label: "ID" },
      { key: "vehicle_id", label: "Vehicle ID" },
      { key: "service_date", label: "Service Date" },
      { key: "description", label: "Description" },
      { key: "mileage", label: "Mileage" }
    ],

    fields: [
      {
        key: "vehicle_id",
        label: "Vehicle ID",
        type: "number"
      },
      {
        key: "service_date",
        label: "Service Date",
        type: "date"
      },
      {
        key: "description",
        label: "Description",
        type: "text"
      },
      {
        key: "mileage",
        label: "Mileage",
        type: "number"
      }                  
    ],

    emptyRecord: {
      vehicle_id: "",
      service_date: "",
      description: "",
      mileage: ""
    }
  }
};

function normalizeRecord(databaseName, record) {
  const normalizedRecord = {
    ...record
  };

  if (databaseName === "vehicles") {
    normalizedRecord.year = Number(
      normalizedRecord.year
    );

    normalizedRecord.customer_id = Number(
      normalizedRecord.customer_id
    );
  }

  if (databaseName === "services") {
    normalizedRecord.vehicle_id = Number(
      normalizedRecord.vehicle_id
    );

    normalizedRecord.mileage = Number(
      normalizedRecord.mileage
    );
  }

  return normalizedRecord;
}

function App() {

// State variables
  const [selectedDatabase, setSelectedDatabase] = useState("customers");

  const [records, setRecords] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const [formData, setFormData] = useState(DATABASES.customers.emptyRecord)
  const [editingId, setEditingId] = useState(null);

// Configuration

  const configuration = DATABASES[selectedDatabase];

// useEffect
  useEffect(() => {
    setEditingId(null);

    setFormData({
      ...DATABASES[selectedDatabase].emptyRecord
    });

    loadRecords();
  }, [selectedDatabase]);

// Loading information  
  async function loadRecords() {
    setLoading(true);
    setError("");

    try {
      const data = await getRecords(
        selectedDatabase
      );
      
      setRecords(data);
    } catch (requestError) {
      setError(requestError.message);
    } finally {
      setLoading(false);
    }
  }


// Changing the Form field  
  function handleInputChange(event) {
    const { name, value } = event.target;

    setFormData((currentData) => ({
      ...currentData,
      [name]: value
    }));
  }

// Adding new data
  async function handleSubmit(event) {
    event.preventDefault();

    setError("");

    try {
      const record = normalizeRecord(
        selectedDatabase,
        formData
      );

      if (editingId === null) {
        await createRecord(
          selectedDatabase,
          record
        );
      } else {
        await updateRecord(
          selectedDatabase,
          editingId,
          record
        );
      }  


      resetForm();

      await loadRecords();
    } catch (requestError) {
      setError(requestError.message);
    }
  }

// Editing data

  function startEditing(record) {
    const editableRecord = { ...record };

    delete editableRecord.id;

    setEditingId(record.id);
    setFormData(editableRecord);
  }

// Form Reset

  function resetForm() {
    setEditingId(null);

    setFormData({
      ...DATABASES[selectedDatabase].emptyRecord
    });
  }


// Delete Row
  async function handleDelete(recordId) {
    const confirmed = window.confirm(
      "Are you sure you want to delete this record?"
    );

    if(!confirmed) {
      return;
    }

    setError("");

    try{
      await deleteRecord(
        selectedDatabase,
        recordId
      );

      if (editingId === recordId) {
        resetForm();
      }

      await loadRecords();
    } catch (requestError) {
      setError(requestError.message);
    }
  }


// User Interface
  return (
    <main className="app">
      <header className="page-header">


        <h1> Multi-Database Management System</h1>
        <p className="subtitle">Manage data across three PostgreSQL databases.</p>
      </header>

      {/* Database Selection */}
      <nav className="database-tabs">
        <button
          type="button"
          className={
            selectedDatabase === "customers"
            ? "database-tab active"
            : "database-tab"
          }
          onClick={() =>
            setSelectedDatabase("customers")
          }
        >
          Customers
        </button>
        
        <button
          type="button"          
          className={
            selectedDatabase === "vehicles"
            ? "database-tab active"
            : "database-tab"
          }
          onClick={() =>
            setSelectedDatabase("vehicles")
          }
        >
          Vehicles
          </button>

        <button
          type="button"
          className={
            selectedDatabase === "services"
            ? "database-tab active"
            : "database-tab"
          }
          onClick={() =>
            setSelectedDatabase("services")
          }
        >
          Services
        </button>
      </nav>

      {/* Error */}
      {error && (
        <div className="error-message">
          {error}
        </div>
      )} 

      <div className="content-grid">
        <section className="card records-card">
          <div className="section header">
            <div>
              <p className="subtitle">
                Selected database
              </p>
              
              <h2>{configuration.title}</h2>
            </div>

            <button 
              type="button"
              className="secondary-button"
              onClick={loadRecords}>
              Refresh
            </button>
          </div>



          {loading ? (
            <p className="status-message">
              Loading records...
            </p>
          ) : records.length === 0 ? (
            <p className="status-message">
              No records found.
            </p>
          ) : (
            <div className="table-wrapper">
              <table>
                <thead>
                  <tr>
                    {configuration.columns.map(
                      (column) => (
                        <th key={column.key}>
                          {column.label}
                        </th>
                      )
                    )}
                  
                  <th>Actions</th>
                </tr>
              </thead>
              
              <tbody>
                {records.map((record) => (
                  <tr key={record.id}>
                    
                    {configuration.columns.map(
                        (column) => (
                        <td key={column.key}>
                          {record[column.key]}
                        </td>
                      )
                    )}
                  
                    <td className="actions">
                      <button
                        type="button"
                        className="edit-button"
                        onClick={() =>
                        startEditing(record)}>
                        Edit
                      </button>
                      
                      <button
                        type="button"
                        className="delete-button"
                        onClick={() =>
                        handleDelete(record.id)}>
                        Delete
                      </button>
                    </td>
                  
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      
        </section>

        {/* Add / Edit form */}
      
        <section className="card form-card">
      
          <p className="subtitle">
            {editingId === null
              ? "Create record"
              : `Editing record ${editingId}`}
          </p>

          <h2>
            {editingId === null
              ? "Add New Record"
              : "Update Record"}
          </h2>

          <form onSubmit={handleSubmit}>
            
            {configuration.fields.map(
              (field) => (
              <label
                key={field.key}
                htmlFor={field.key}
                className="form-field"
              >
                {field.label}

                <input
                  id={field.key}
                  required
                  type={field.type}
                  name={field.key}
                  value={formData[field.key]}
                  onChange={handleInputChange}
                />
                </label>
              )
            )}

        
        
            <div className="form-actions">

              <button
                type="submit"
                className="primary-button"
                >
                  {editingId === null
                    ? "Add Record"
                    : "Save Changes"}
              </button>

              {editingId !== null && (
                <button
                  type="button"
                  className="secondary-button"
                  onClick={resetForm}
                  >
                  Cancel
                </button>
              )}

            </div>

          </form>

        </section>

      </div>

    </main>
  );
}

export default App;