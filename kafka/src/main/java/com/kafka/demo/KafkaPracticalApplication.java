package com.kafka.demo;

import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.apache.kafka.clients.consumer.ConsumerRecords;
import org.apache.kafka.clients.consumer.KafkaConsumer;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.time.Duration;
import java.util.Collections;
import java.util.Properties;

// NOTE :- Run this commands on the same file path to execute the code
// mvn compile
// mvn exec:java -Dexec.mainClass="com.kafka.demo.KafkaPracticalApplication"

public class KafkaPracticalApplication {
	private static final String URL = "jdbc:sqlserver://localhost:1433;databaseName=YourDatabase";
	private static final String USER = "yourUsername";
	private static final String PASSWORD = "yourPassword";
	private static final String TOPIC = "yourTopic";
	private static final String BOOTSTRAP_SERVERS = "localhost:9092";

	public static void main(String[] args) {
		Properties props = new Properties();
		props.put("bootstrap.servers", BOOTSTRAP_SERVERS);
		props.put("group.id", "test-group");
		props.put("key.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");
		props.put("value.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");
		KafkaConsumer<String, String> consumer = new KafkaConsumer<>(props);
		consumer.subscribe(Collections.singletonList(TOPIC));

		while (true) {
			ConsumerRecords<String, String> records = consumer.poll(Duration.ofMillis(100));
			for (ConsumerRecord<String, String> record : records) {
				storeInDatabase(record.value());
			}
		}
	}

	private static void storeInDatabase(String data) {
		String sql = "INSERT INTO KafkaData (data) VALUES (?)";
		try (Connection conn = DriverManager.getConnection(URL, USER, PASSWORD);
			 PreparedStatement pstmt = conn.prepareStatement(sql)) {
			pstmt.setString(1, data);
			pstmt.executeUpdate();
			System.out.println("Stored: " + data);
		} catch (SQLException e) {
			e.printStackTrace();
		}
	}
}