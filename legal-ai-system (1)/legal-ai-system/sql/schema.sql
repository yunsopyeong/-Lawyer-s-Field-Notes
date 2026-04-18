CREATE TABLE content_sources (
    id SERIAL PRIMARY KEY,
    raw_text TEXT,
    sanitized_text TEXT,
    category VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE content_drafts (
    id SERIAL PRIMARY KEY,
    source_id INT REFERENCES content_sources(id),
    content TEXT,
    status VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE publish_queue (
    id SERIAL PRIMARY KEY,
    draft_id INT REFERENCES content_drafts(id),
    platform VARCHAR(20),
    status VARCHAR(20),
    scheduled_at TIMESTAMP
);
