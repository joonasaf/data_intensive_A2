async function request(path, options = {}) {
    const response = await fetch(path, {
        headers: {
            "Content-Type": "application/json",
            ...options.headers
        },
        ...options
    });

    if (response.status === 204) {
        return null;
    }

    const data = await response.json();
    
    if (!response.ok) {
        const message =
            typeof data.detail === "string"
                ?data.detail
                : "The request failed.";
        throw new Error(message);
        
    }

    return data;
}

export function getRecords(databaseName) {
    return request(`/api/${databaseName}`);
}

export function createRecord(databaseName, record) {
    return request(`/api/${databaseName}`, {
        method: "POST",
        body: JSON.stringify(record)
    });
}

export function updateRecord(databaseName, id, record) {
    return request(`/api/${databaseName}/${id}`, {
        method: "PUT",
        body: JSON.stringify(record)
    });
}

export function deleteRecord(databaseName, id) {
    return request (`/api/${databaseName}/${id}`, {
        method: "DELETE"
    });
}