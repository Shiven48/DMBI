package com.example;

import org.apache.flink.api.common.functions.MapFunction;
import org.apache.flink.api.java.tuple.Tuple2;
import org.apache.flink.connector.jdbc.JdbcConnectionOptions;
import org.apache.flink.connector.jdbc.JdbcExecutionOptions;
import org.apache.flink.connector.jdbc.JdbcSink;
import org.apache.flink.streaming.api.datastream.DataStream;
import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment;
import java.sql.PreparedStatement;

public class SimpleFlinkJdbcExample {
    public static void main(String[] args) throws Exception {
        // Set up the streaming execution environment
        final StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();

        // Create a simple DataStream (you can replace this with Kafka or other sources)
        DataStream<String> dataStream = env.fromElements(
                "record1",
                "record2",
                "record3",
                "record4",
                "record5"
        );

        // Transform data if needed
        DataStream<Tuple2<String, Integer>> processedStream = dataStream
                .map(new MapFunction<String, Tuple2<String, Integer>>() {
                    @Override
                    public Tuple2<String, Integer> map(String value) {
                        // Simple processing - convert to uppercase and add a counter
                        return new Tuple2<>(value.toUpperCase(), value.length());
                    }
                });

        // Print the processed data to console
        processedStream.print();

        // Set up JDBC sink to store data in a database
        processedStream.addSink(
                JdbcSink.sink(
                        // SQL statement to execute for each record
                        "INSERT INTO data_records (text, length) VALUES (?, ?)",

                        // Prepare statement with data from the tuple
                        (PreparedStatement statement, Tuple2<String, Integer> tuple) -> {
                            statement.setString(1, tuple.f0);
                            statement.setInt(2, tuple.f1);
                        },

                        // JDBC execution options (batch size, interval, etc.)
                        JdbcExecutionOptions.builder()
                                .withBatchSize(1000)
                                .withBatchIntervalMs(200)
                                .withMaxRetries(5)
                                .build(),

                        // JDBC connection options
                        new JdbcConnectionOptions.JdbcConnectionOptionsBuilder()
                                .withUrl("jdbc:sqlserver://localhost:1433;databaseName=YourDatabase")
                                .withDriverName("com.microsoft.sqlserver.jdbc.SQLServerDriver")
                                .withUsername("yourUsername")
                                .withPassword("yourPassword")
                                .build()
                )
        );

        // Execute the Flink job
        env.execute("Simple Flink JDBC Example");
    }
}